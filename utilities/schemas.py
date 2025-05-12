class SchemasDummy:

    user_list_schema = {
            "type": "object",
            "properties": {
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "title": {"type": "string"},
                            "firstName": {"type": "string"},
                            "lastName": {"type": "string"},
                            "picture": {"type": "string"}},
                        "required": [
                            "id",
                            "firstName",
                            "lastName"]
                    }
                },
                "total": {"type": "number"},
                "page": {"type": ["number", 'null']},
                "limit": {"type": ["number", 'null']}
            },
            "required": [
                "data",
                "total",
                "page",
                "limit"
            ]
        }

    post_list_schema = {
          "type": "object",
          "properties": {
            "data":
                {"type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {"type": "string"},
                  "image": {"type": "string"},
                  "likes": {"type": "number"},
                  "tags": {
                    "type": "array",
                    "items": {"type": "string"}
                  },
                  "text": {"type": "string"},
                  "publishDate": {"type": "string"},
                  "updatedDate": {"type": "string"},
                  "owner": {
                    "type": "object",
                    "properties": {
                      "id": {"type": "string"},
                      "firstName": {"type": "string"},
                      "lastName": {"type": "string"},
                      "title": {"type": "string"},
                      "picture": {"type": "string"}
                    },
                    "required": [
                      "id",
                      "firstName",
                      "lastName"
                    ]
                  }
                },
                "required": [
                  "id"
                ]
              }
            },
            "total": {"type": "number"},
            "page": {"type": ["number", 'null']},
            "limit": {"type": ["number", 'null']}
          },
          "required": [
            "data",
            "total",
            "page",
            "limit"
          ]
        }