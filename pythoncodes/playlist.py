from textual.app import App
from textual.widgets import Header, Footer, Button, ListView, ListItem, Static
from textual.containers import VerticalScroll, Horizontal, Container
from rich.text import Text
import random

class PlaylistApp(App):
    def __init__(self):
        super().__init__()
        self.playlist = []

    def compose(self):
        yield Header()
        yield Footer()
        yield Container(
            Horizontal(
                Button("Add Song", id="add-song", variant="primary"),
                Button("Shuffle Playlist", id="shuffle-playlist"),
                Button("Clear Playlist", id="clear-playlist", variant="error"),
            ),
            id="controls",
        )
        yield VerticalScroll(ListView(), id="playlist-view")
        yield Static("No songs in the playlist yet.", id="info")

    def on_button_pressed(self, event):
        if event.button.id == "add-song":
            self.add_song()
        elif event.button.id == "shuffle-playlist":
            self.shuffle_playlist()
        elif event.button.id == "clear-playlist":
            self.clear_playlist()

    def add_song(self):
        new_song = self.prompt_for_song()
        if new_song:
            self.playlist.append(new_song)
            self.update_playlist_view()

    def prompt_for_song(self):
        song_title = input("Enter song title: ")
        song_duration = input("Enter song duration (e.g., 3:45): ")
        return {"title": song_title, "duration": song_duration}

    def update_playlist_view(self):
        playlist_view = self.query_one("#playlist-view", ListView)
        playlist_view.clear()

        if self.playlist:
            for song in self.playlist:
                item = ListItem(Text(f"{song['title']} ({song['duration']})"))
                playlist_view.append(item)
        else:
            self.query_one("#info", Static).update("No songs in the playlist yet.")

    def shuffle_playlist(self):
        if self.playlist:
            random.shuffle(self.playlist)
            self.update_playlist_view()

    def clear_playlist(self):
        self.playlist.clear()
        self.update_playlist_view()

PlaylistApp().run()