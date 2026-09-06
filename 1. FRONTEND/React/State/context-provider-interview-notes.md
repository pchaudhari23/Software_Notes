# Context API / Provider Pattern — Interview Notes

Scope: `createContext`, `useContext`, custom provider components, and how this compares to Redux. Interviewers use this to test whether you know *when* Context is enough and *why* it isn't a drop-in Redux replacement.

---

## 1. What problem does Context solve?

- Pure prop-drilling fix: passing data through many layers of components that don't themselves need it, just to reach a deeply nested child.
- Context lets any descendant of a `Provider` read a value directly via `useContext`, skipping the intermediate layers.
- It is **not** a state management library by itself — it has no actions, reducers, middleware, or devtools. It's a plumbing mechanism for passing values down the tree. State management is something you build on top of it (usually with `useState` or `useReducer` inside the provider).

## 2. Basic shape

```jsx
import { createContext, useContext, useState } from 'react';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = () => setUser({ id: 1, name: 'Pritam' });
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider');
  return ctx;
}
```

- `createContext(defaultValue)` — the argument is only used if a component calls `useContext` **without** any matching `Provider` above it in the tree. Passing `null` and guarding with a thrown error (as above) is a common, deliberate pattern — it turns a silent "undefined behavior" bug into a loud, immediate one during development.
- The custom `useAuth()` hook wrapping `useContext` is a widely expected pattern — interviewers may ask "why not just call `useContext(AuthContext)` directly everywhere?" Answer: centralizes the null-check, hides the context object as an implementation detail, and makes future refactors (e.g., splitting the context) not require touching every consumer.

## 3. Provider nesting ("provider hell")

```jsx
<AuthProvider>
  <UIProvider>
    <DataProvider>
      <ModalProvider>
        <App />
      </ModalProvider>
    </DataProvider>
  </UIProvider>
</AuthProvider>
```

- Each concern (auth, UI state, data, modal) gets its own context/provider — a common pattern once an app has more than one or two pieces of shared state.
- **This nesting is itself a well-known criticism of Context at scale** — often called "provider hell" or "wrapper hell." It's a legitimate talking point for "why Redux over Context" (Redux needs exactly one `<Provider store={store}>` regardless of how many slices exist).
- Order matters when providers depend on each other (see below) — this is fragile in a way Redux's single store isn't.

## 4. Cross-context dependencies (a real design smell to know)

```jsx
export function DataProvider({ children }) {
  const { user } = useAuth();       // depends on AuthProvider being an ancestor
  const { setLoading, setError } = useUI(); // depends on UIProvider being an ancestor
  // ...
}
```

- A provider calling another context's hook internally creates a **hidden ordering dependency** — `DataProvider` will throw at runtime if it's not nested under both `AuthProvider` and `UIProvider`, but nothing in the type system or file structure makes that obvious.
- This is a genuinely strong point to raise if asked "what are the downsides of Context at scale": the coupling isn't visible until you either read every provider's internals or hit the runtime error. Redux doesn't have this problem — any reducer/saga can read any part of the store via `getState()`/`select()` without an ancestor requirement.
- Interview framing: "Context couples providers to tree position; Redux couples nothing to position because there's one store."

## 5. Re-render behavior (frequently tested)

- **Every component that calls `useContext(SomeContext)` re-renders whenever that context's value changes** — there is no built-in selector mechanism like Redux's `useSelector`/`connect` shallow-compare.
- This gets expensive if a context value bundles many unrelated pieces of state together (e.g., one giant `AppContext` holding auth, theme, and data all in one object) — a change to any one field re-renders every consumer of the whole context, even ones that only cared about a different field.

**The fix pattern (know this cold):**
1. **Split contexts by concern** — separate `AuthContext`, `UIContext`, `DataContext` instead of one mega-context (this is *why* the multi-provider pattern above exists — it's not just organizational, it's a performance necessity).
2. **Memoize the value object** passed to `Provider`:

```jsx
const value = useMemo(() => ({ user, login, logout }), [user]);
return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
```

Without `useMemo`, the value object is a **new object reference every render** of the provider, which defeats even React's own bail-out optimizations for consumers — every re-render of the provider forces every consumer to re-render too, regardless of whether the actual data changed.

> Worth knowing: even Context's official React docs flag this — Context is not optimized for high-frequency updates, specifically because of this re-render-all-consumers behavior.

## 6. useContext + useReducer (the "poor man's Redux")

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
return <MyContext.Provider value={{ state, dispatch }}>{children}</MyContext.Provider>;
```

- This combo gets you actions + a reducer + a shared value, which looks a lot like Redux's shape — and it's a legitimate, commonly recommended pattern for medium-sized apps that don't want a full Redux setup.
- What it still lacks versus Redux: no middleware layer (no clean way to intercept dispatch for async/logging), no devtools/time-travel debugging, no built-in memoized selectors, and (per above) no partial re-render optimization without manual `useMemo`/context-splitting.
- Likely interview question: "When would you reach for `useReducer` + Context instead of Redux?" — good answer: single, moderately complex piece of shared state (e.g., a multi-step form, a shopping cart in a small app), not deeply nested/relational data, no need for middleware-driven async orchestration or time-travel debugging.

## 7. Context vs Redux — comparison table

| | Context API | Redux |
|---|---|---|
| Purpose | Pass values down the tree, avoid prop drilling | Full state management: predictable updates, middleware, devtools |
| Re-render granularity | Every consumer re-renders on any value change (unless split/memoized) | Only components whose selected slice changed re-render |
| Async/side effects | Nothing built in — hand-roll with `useEffect` inside provider | Middleware ecosystem (thunk, saga) purpose-built for this |
| DevTools / time-travel | None | Redux DevTools — action log, state diffing, time travel |
| Boilerplate for simple cases | Minimal | More setup (store, slices/reducers, actions) |
| Cross-cutting, high-frequency state | Weak fit (re-render cost, no selectors) | Strong fit |
| Scaling with many independent slices | Provider nesting gets unwieldy ("provider hell") | Single store, `combineReducers`/multiple slices, no nesting cost |

**Standard framing to give in an interview:** Context is a *dependency injection mechanism*, not a state manager. It's the right tool for low-frequency, narrowly-scoped shared values (theme, locale, auth flag, feature flags). Once you have complex, frequently-changing, cross-cutting state — or need middleware for async orchestration — Redux (or Zustand, Jotai, etc.) is the better fit specifically because of the re-render granularity and middleware gaps above.

## 8. Common mistakes / gotchas

- **One giant context for the whole app** — the single biggest anti-pattern; causes broad re-renders and makes the provider a dumping ground with no clear ownership.
- **Not memoizing the provider's value prop** — silently defeats React's re-render optimizations; easy to miss because nothing errors, it's just slower than it should be.
- **Cross-context coupling inside providers** (as in section 4) — creates invisible ordering requirements between providers.
- **Using Context for very high-frequency updates** (e.g., mouse position, animation frame state, form input on every keystroke across a large tree) — the re-render-all-consumers behavior makes this a poor fit; local `useState` in the component that actually needs it is almost always better.
- **Forgetting the null/undefined guard in the custom hook** — calling `useContext` outside its provider silently returns the `createContext` default (often `null`/`undefined`), which then fails later in a confusing way (e.g., "cannot read property of undefined") far from the actual root cause. The `if (!ctx) throw ...` guard turns this into an immediate, clear error.

## 9. Quick-fire Q&A

**Q: Does updating Context state trigger reducer-like pure updates the way Redux does?**
A: No — Context itself has no concept of reducers. If you use `useState` inside the provider, updates go through React's normal state update rules directly. If you use `useReducer` inside the provider (common), then yes, you get reducer-style pure updates, but that's `useReducer`'s behavior, not something Context provides on its own.

**Q: Can Context replace Redux entirely?**
A: For small-to-medium apps, `useReducer` + Context can substitute for Redux with less setup. It becomes a weaker substitute as the app grows — you lose middleware, devtools, and automatic selector-based re-render optimization, and you start hand-building things (memoized values, split contexts) that Redux gives you for free structurally.

**Q: Why might you split one context into several rather than one big one?**
A: To limit re-render blast radius — consumers of `AuthContext` shouldn't re-render when unrelated `ModalContext` state changes. Splitting by concern (as in the multi-provider example) is the direct fix for Context's lack of built-in selectors.

**Q: What's the actual mechanism causing "every consumer re-renders"?**
A: React re-renders every component that calls `useContext(X)` whenever `X.Provider`'s `value` prop changes by reference (not by deep equality) — so both an actual data change *and* an unmemoized new object literal every render will trigger it.

**Q: Is there a way to get selector-like behavior with Context?**
A: Not natively — you'd need to split contexts finely enough that each one only holds what a given group of consumers cares about, or use a third-party library (e.g., `use-context-selector`) that adds selector semantics on top of Context. Worth mentioning if asked "how would you fix this at scale" — shows awareness beyond the built-in API.

---

## Summary table: Context API surface

| API | Purpose |
|---|---|
| `createContext(defaultValue)` | Creates a context object; `defaultValue` only applies with no ancestor `Provider` |
| `<Context.Provider value={...}>` | Supplies the value to all descendant consumers |
| `useContext(Context)` | Reads the nearest ancestor `Provider`'s value |
| Custom `useX()` hook wrapping `useContext` | Idiomatic pattern — centralizes null-checks, hides context object |
| `useReducer` (paired with Context) | Adds reducer-style state updates on top of Context, closer to a mini-Redux |
| `useMemo` on the `value` prop | Required to avoid forcing all consumers to re-render every provider render |
