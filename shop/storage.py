from typing import Any

from shop.errors import ConflictError, NotFoundError


class Storage:
    def __init__(self):
        self.models = {}
        self.model_names = set()
        self.last_id = 0

    def check_model_name_unique(self, name):
        return name not in self.model_names

    def get_by_id(self, model_id):
        model = self.models.get(model_id)
        if not model:
            raise NotFoundError('model', f'id: {model_id}')
        return model

    def delete(self, model_id):
        model = self.get_by_id(model_id)
        self.model_names.remove(model['name'])
        self.models.pop(model_id)

    def get_all(self):
        return list(self.models.values())

    def add(self, model):
        if not self.check_model_name_unique(model['name']):
            raise ConflictError('model', f'name: {model["name"]}')
        self.last_id += 1
        model['id'] = self.last_id
        self.models[model['id']] = model
        self.model_names.add(model['name'])
        return model

    def change(self, model_id: int, change_model: dict[str, Any]) -> dict[str, Any]:

        if model_id not in self.models.keys():
            raise NotFoundError('model', f'id: {model_id}')
        old_model = self.models[model_id]  # noqa: WPS204
        old_name = old_model['name']
        new_name = change_model['name']

        if old_name == new_name:
            self.models[model_id] = change_model
            return self.models[model_id]

        if old_name != new_name and self.check_model_name_unique(new_name):
            self.model_names.remove(old_name)
            self.model_names.add(new_name)
            self.models[model_id] = change_model
            return self.models[model_id]

        raise ConflictError('model', f'name: {new_name}')
