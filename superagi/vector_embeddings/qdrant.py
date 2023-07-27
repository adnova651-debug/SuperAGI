from typing import Any
from superagi.vector_embeddings.base import VectorEmbeddings

class Qdrant(VectorEmbeddings):

    @classmethod
    def get_vector_embeddings_from_chunks(cls, chunk_json: Any, uuid, metadata, embeds):
        """ Returns embeddings for vector dbs from final chunks"""
        final_chunks = []
        result = {}
        if chunk_json != {}:
            for key in chunk_json.keys():
                final_chunks.append(chunk_json[key])

            uuid = []
            embeds = []
            metadata = []
            for i in range(0, len(final_chunks)):
                uuid.append(final_chunks[i]["id"])
                embeds.append(final_chunks[i]["embeds"])
                data = {
                    'text': final_chunks[i]['text'],
                    'chunk': final_chunks[i]['chunk'],
                    'knowledge_name': final_chunks[i]['knowledge_name']
                }
                metadata.append(data)
            result['ids'] = uuid
            result['payload'] = metadata
            result['vectors'] = embeds

        return result