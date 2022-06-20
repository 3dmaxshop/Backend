from typing import Any

from shop.errors import ConflictError, NotFoundError


class Storage:
    def __init__(self):
        self.models = {}
        self.model_names = set()
        self.last_uid = 0

    def check_model_name_unique(self, name):
        return name not in self.model_names

    def get_by_uid(self, model_uid):
        model = self.models.get(model_uid)
        if not model:
            raise NotFoundError('model', f'uid: {model_uid}')
        return model

    def delete(self, model_uid):
        model = self.get_by_id(model_uid)
        self.model_names.remove(model['name'])
        self.models.pop(model_uid)

    def get_all(self):
        return list(self.models.values())

    def add(self, model):
        if not self.check_model_name_unique(model['name']):
            raise ConflictError('model', f'name: {model["name"]}')
        self.last_uid += 1
        model['uid'] = self.last_uid
        self.models[model['uid']] = model
        self.model_names.add(model['name'])
        return model

    def change(self, model_uid: int, change_model: dict[str, Any]) -> dict[str, Any]:

        if model_uid not in self.models.keys():
            raise NotFoundError('model', f'uid: {model_uid}')
        old_model = self.models[model_uid]  # noqa: WPS204
        old_name = old_model['name']
        new_name = change_model['name']

        if old_name == new_name:
            self.models[model_uid] = change_model
            return self.models[model_uid]

        if old_name != new_name and self.check_model_name_unique(new_name):
            self.model_names.remove(old_name)
            self.model_names.add(new_name)
            self.models[model_uid] = change_model
            return self.models[model_uid]

        raise ConflictError('model', f'name: {new_name}')
