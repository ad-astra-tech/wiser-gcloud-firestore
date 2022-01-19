from wiser.gcloud.firestore.services import Firestore
from wiser.gcloud.firestore.types import (
    FirestoreCollectionBuilder,
)

COLLECTION_NAME = "collection_name"

collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name=COLLECTION_NAME)
    .build()
)

Firestore.delete_collection(collection=collection)
