from starlette_admin.contrib.sqla import ModelView



class UserView(ModelView):
    fields = ['id', 'email', 'hashed_password','username','first_name', 'last_name', 'birthdate', 'is_active', 'is_staff', 'is_superuser']


class GameView(ModelView):
    fields = ['id', 'title', 'description', 'start_time', 'end_time', 'topic',  'score']


class QuestionView(ModelView):
    fields = ['id', 'title', 'description', 'topic']


class ParticipationView(ModelView):
    fields = ['id', 'user', 'game', 'start_time', 'end_time', 'gained_score']


class SubmissionView(ModelView):
    fields = ['id', 'owner', 'game', 'question', 'option', 'is_correct']


class OptionView(ModelView):
    fields = ['id', 'question', 'title', 'is_correct']


class TopicView(ModelView):
    fields = ['id', 'name']

