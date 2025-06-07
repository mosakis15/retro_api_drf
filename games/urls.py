from django.urls import path
from .views import RetroGameListCreateView, RetroGameRetrieveUpdateDeleteView, add_game

urlpatterns = [
    path('retro-games/', RetroGameListCreateView.as_view(), name='retrogame-list-create'),
    path('retro-games/<int:pk>/', RetroGameRetrieveUpdateDeleteView.as_view(), name='retrogame-detail'),
    path('add-game/', add_game, name='game-form'),
]
