import json

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes


def get_ml_fields(local_path: str):
    secrete = json.load(open('albumy/blueprints/secrete.json'))
    API_KEY = secrete['API_KEY']
    END_POINT = secrete['END_POINT']
    client = ComputerVisionClient(END_POINT, CognitiveServicesCredentials(API_KEY))
    try:
        alt_respond = client.describe_image_in_stream(
            open(local_path, 'rb'),
            raw=True
        )
        text = alt_respond.output.captions[0].text

        tag_respond = client.tag_image_in_stream(
            open(local_path, 'rb')
        ).tags
        tags = []
        for tag in tag_respond:
            tags.append(tag.name)

    except:
        print("Error occur when fetching alternating text from azure")

    return text, tags

