from typing import Any
from shop.errors import AppError, NotFoundError, Conflict, IndexNotFoundError


class Storage:
    def __init__(self):
        self.models = {}
        self.model_names = set()
        self.last_id = 0

    def check_model_name_unique(self,name):
        return name not in self.model_names
         
    def get_by_id(self, model_id):
        return self.models.get(model_id)

    def delete(self, model_id):
        model = self.models[model_id]
        model_name = model['name']
        self.model_names.remove(model_name)
        self.models.pop(model_id)
    
    def get_all(self):
        return list(self.models.values())

    def add(self, model):
        self.last_id += 1
        model['id'] = self.last_id
        self.models[model['id']] = model
        self.model_names.add(model['name'])

    def change(self, model_id:int, change_model:dict[str, Any]) -> dict[str, Any]:

        if model_id not in self.models.keys():
            raise IndexNotFoundError(f'reason: model id {model_id} not found')

        old_name = self.models[model_id]['name']
        new_name = change_model['name']

        if old_name == new_name:
            self.models[model_id] = change_model
            return self.models[model_id]

        if old_name != new_name and self.check_model_name_unique(new_name):
            self.model_names.remove(old_name)
            self.model_names.add(new_name)
            self.models[model_id] = change_model
            return self.models[model_id]
            
        raise Conflict(change_model, f'reason: model name {new_name} is not unique')   
        