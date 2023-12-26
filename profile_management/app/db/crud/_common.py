from pymongo.collection import Collection


def create_document(collection: Collection, document: dict) -> str:
    """ Function to insert a document into a collection and
    return the document's id. """
    return str(collection.insert_one(document).inserted_id)


def get_document(collection: Collection, elements: dict) -> dict | None:
    """ Function to retrieve single document from a provided
    Collection using a dictionary containing a document's elements. """
    return collection.find_one(elements)


def get_documents(collection: Collection, elements: dict) -> list[dict]:
    """ Function to retrieve multiple documents from a provided
    Collection using a dictionary containing a document's elements. """
    return [item for item in collection.find(elements)]


def update_document(collection: Collection, query_elements: dict, new_values: dict) -> None:
    """ Function to update a single document in a collection. """
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection: Collection, query: dict) -> None:
    """ Function to delete a single document from a collection. """
    collection.delete_one(query)
