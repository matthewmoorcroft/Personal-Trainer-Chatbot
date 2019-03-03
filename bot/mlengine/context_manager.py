

class ContextManager:
    def __init__(self):
        self.context_list = []

    def get_context(self, id):
        for c in self.context_list:
            if c["id"] == id:
                return c
        return False

    def check_context(self, id):
        for c in self.context_list:
            if c["id"] == id:
                return True
        return False

    def update_context(self, context):
        count = 0
        for c in self.context_list:
            if context["id"] == c["id"]:
                self.context_list[count] = context
                return True
            count += 1
        return False

    def remove_context(self, context):
        count = 0
        for c in self.context_list:
            if context["id"] == c["id"]:
                self.context_list.pop(count)
                return True
            count += 1
        return False

    def add_context(self, context):
        self.remove_context(context)
        self.context_list.append(context)

      # def check_freshness (self, context):
      #     if context
    def create_context(self, data, welcome_process=True):

        context = {}

        context['id'] = data['user']['id']
        context["process_flow_id"] = None
        context["process_flow"] = None
        context["new_message"] = data
        context["message_history"] = []
        context["data_storage"] = []
        context["data_extracted"] = []
        context["step_current"] = None
        context["awaiting_user_action"] = False
        context["first_iteration"] = True
        context["data_found"] = []
        context["data_found_new"] = []
        context["incorrect_answers"] = 0

        return context
