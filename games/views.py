from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import RetroGame
from .serializers import RetroGameSerializer
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from .forms import RetroGameForm

class RetroGameListCreateView(generics.ListCreateAPIView):
    queryset = RetroGame.objects.all()
    serializer_class = RetroGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'platform', 'release_date']

    def perform_create(self, serializer):
        serializer.save()

class RetroGameRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RetroGame.objects.all()
    serializer_class = RetroGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def add_game(request):
    if request.method == 'POST':
        form = RetroGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game-form')
    else:
        form = RetroGameForm()
    return render(request, 'games/game_form.html', {'form': form})
