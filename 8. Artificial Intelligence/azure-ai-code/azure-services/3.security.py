from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


def main():
    global ai_endpoint
    global cog_key

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        key_vault_name = os.getenv('KEY_VAULT')
        app_tenant = os.getenv('TENANT_ID')
        app_id = os.getenv('APP_ID')
        app_password = os.getenv('APP_PASSWORD')

        # Get Azure AI services key from keyvault using the service principal credentials
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
        credential = ClientSecretCredential(app_tenant, app_id, app_password)
        keyvault_client = SecretClient(key_vault_uri, credential)
        secret_key = keyvault_client.get_secret("AI-Services-Key")
        cog_key = secret_key.value

        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                language = GetLanguage(userText)
                print('Language:', language)

    except Exception as ex:
        print(ex)

def GetLanguage(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name


if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------------------------

# In Terminal:
# pip install azure-ai-textanalytics==5.3.0
# pip install azure-identity==1.5.0
# pip install azure-keyvault-secrets==4.2.0
# python keyvault-client.py

#--------------------------------------------------------------------------------------------------

# CLI COMMAND:
# 1.Retrive keys: az cognitiveservices account keys list --name <resourceName> --resource-group <resourceGroup>
# 2.Regenerate keys: az cognitiveservices account keys regenerate --name <resourceName> --resource-group <resourceGroup> --key-name key1
# 3.Creating a service principal:  az ad sp create-for-rbac -n "api://<spName>" --role owner --scopes subscriptions/<subscriptionId>/resourceGroups/<resourceGroup>
# az ad sp show --id <appId>
# az keyvault set-policy -n <keyVaultName> --object-id <objectId> --secret-permissions get list

#Login in terminal without CLI: az login
#See subscription information: az account show
#Logout of terminal: az logout

#--------------------------------------------------------------------------------------------------
