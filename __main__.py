from views import MainView
from seed_data import initialize_seed_data

initialize_seed_data()

view = MainView()
view.prepare_view()

view.render()
