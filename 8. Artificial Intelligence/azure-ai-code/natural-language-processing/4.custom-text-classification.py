# STEPS TO FOLLOW ON PORTAL:
# 1.Create Language resource, select custom text classification 
# 2.Language studio portal -  https://language.cognitive.azure.com/
# 3.Upload sample articles (text files) to blob storage 
# 4.Create new project - Custom text classification
# 5.Label the data - add new labels and assign the labels to articles (the labels we have added will help to determine custom text)
# 6.Create, train and test the model
# 7.Evaluate the model
# 8.Deploy the model 

# ---------------------------------------------------------------------------------------------------

from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        project_name = os.getenv('PROJECT')
        deployment_name = os.getenv('DEPLOYMENT')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Read each text file in the articles folder
        batchedDocuments = []
        articles_folder = 'articles'
        files = os.listdir(articles_folder)
        for file_name in files:
            # Read the file contents
            text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
            batchedDocuments.append(text)

        # Get Classifications
        operation = ai_client.begin_single_label_classify(
            batchedDocuments,
            project_name=project_name,
            deployment_name=deployment_name
        )

        document_results = operation.result()

        for doc, classification_result in zip(files, document_results):
            if classification_result.kind == "CustomDocumentClassification":
                classification = classification_result.classifications[0]
                print("{} was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            elif classification_result.is_error is True:
                print("{} has an error with code '{}' and message '{}'".format(
                    doc, classification_result.error.code, classification_result.error.message)
                )

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
#  pip install azure-ai-textanalytics==5.3.0