Every folder has 4 files:

1. data_source.json
2. index.json
3. indexer.json
4. skillset.json
5. A command OR cmd file which contains script to run and take inputs from the above files.

- All the files are similar with very minor changes.
- create-search or update-search or modify-search cmd file creates a skillset, index and indexer in the Azure search resource.
- Initially a setup file must be run whose sample output is given below. The script creates three resources in Azure resource group - 1. Azure search, 2. AI Services, 3. Azure storage container
- The things from the below response must be used in the json files mentioned above.
- Azure storage container contains the data for indexing. The data folder contains all the data for storage.
- Right click on the folder containing cmd file and open in integrated terminal in vs code.then run the command - ./setup OR ./create-search etc to run the script.

---
