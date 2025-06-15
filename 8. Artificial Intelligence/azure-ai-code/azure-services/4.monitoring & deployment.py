# MONITORING:
# 1.Create resource
# 2.Create alert rule
# 3.View the metric

# Generate request using:
# curl -X POST "<your-endpoint>/language/:analyze-text?api-version=2023-04-01" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: <your-key>" --data-ascii "{'analysisInput':{'documents':[{'id':1,'text':'hello'}]}, 'kind': 'LanguageDetection'}"

# ---------------------------------------------------------------------------------------------------------------------

# DEPLOYMENT:

# ENV VARIABLES FOR CONTAINER:
# 1.API KEY: Either key for your Azure AI services resource
# 2.BILLING: The endpoint URI for your Azure AI services resource
# 3.EULA: Accept

# Subscription key is not required for client applications which consume AI Services from container, only billing endpoint is required.

# Using the container deployed service:
# curl -X POST "http://<your_ACI_IP_address_or_FQDN>:5000/text/analytics/v3.0/languages" -H "Content-Type: application/json" --data-ascii "{'documents':[{'id':1,'text':'Hello world.'},{'id':2,'text':'Salut tout le monde.'}]}"

# Command to deploy AI Service on docker container instead of ACI:
# docker run --rm -it -p 5000:5000 --memory 12g --cpus 1 mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest Eula=accept Billing=<yourEndpoint> ApiKey=<yourKey>

# ---------------------------------------------------------------------------------------------------------------------
