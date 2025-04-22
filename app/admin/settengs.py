from starlette_admin.contrib.sqla import Admin

from app.database import engine
from app.admin.views import UserView, GameView, SubmissionView, TopicView, ParticipationView, OptionView, QuestionView
from app.models import User, Game, Participation, Submission, Option, Question, Topic


admin = Admin(
    engine,
    title= "Bilimdon Admin"
)

admin.add_view(UserView(User, icon='fa fa-user'))
admin.add_view(GameView(Game, icon='fa fa-trophy'))
admin.add_view(ParticipationView(Participation, icon='fa fa-users'))
admin.add_view(SubmissionView(Submission, icon='fa fa-car'))
admin.add_view(OptionView(Option, icon='fa fa-notes'))
admin.add_view(QuestionView(Question, icon='fa fa-question'))
admin.add_view(TopicView(Topic, icon='fa fa-topic'))

