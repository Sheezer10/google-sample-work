
from .video_library import VideoLibrary
is_playing = False
previous_video = None


def now_playing(args):
    pass


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.video_under_process = None
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)



    def play_video(self, video_id):
        global is_playing
        global previous_video
        """Plays the respective video."""

        """Args: video_id: The video_id to be played."""

        now_playing = self._video_library.get_video(video_id)

        if not now_playing:
            print(f"cannot play video: Video does not exist!")
        else:
            if is_playing is True:
                print(f"Stopping video: {previous_video}")
                print(f"Playing video: {now_playing.title}")
                previous_video = now_playing.title
            else:
                print(f"Playing video: {now_playing.title}")
                is_playing = True
                previous_video = now_playing.title

    def stop_video(self):

        global is_playing
        global previous_video

        """Stops the current video."""
        # check if video playing and stop if true
        if is_playing:
            print(f"Stopping video: {now_playing.title}")
            is_playing = False
            previous_video = None
        # Check if video playing if false, then don't do anything.
        else:
            if not is_playing:
                print("Cannot stop video: No video is currently playing!")
                previous_video = None
    def play_random_video(self):
        
        videos = self._video_library.get_all_videos()

        # if all videos are marked as flagged them showing no video avaiilable for random function
        if len([x for x in videos if x.flagged == None]) == 0:
            print("No videos available")
            return

        vid = videos[random.randint(0, len(videos) - 1)]
        self.play_video(vid._video_id)






    def pause_video(self):
       

        if self.video_under_process.video != None:
            if (self.video_under_process.status != video_state.Pause):
                self.video_under_process.set_status(video_state.Pause)
            else:
                print("Video already paused:", self.video_under_process.video._title)

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
       

        if self.video_under_process.video != None:
            if self.video_under_process.status == video_state.Pause:
                self.video_under_process.set_status(video_state.Continue)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")






    def show_playing(self):
        
        if self.video_under_process.video != None:
            if self.video_under_process.status != video_state.Pause:
                print("Currently playing:", self.get_video_details(self.video_under_process.video))
            else:
                print("Currently playing:", self.get_video_details(self.video_under_process.video), "- PAUSED")

        else:
            print("No video is currently playing")

   
    def is_playlist_exist(self, name):
        return name in self.playlists.keys()

    def create_playlist(self, playlist_name):
      

        pln = playlist_name.lower()
        if pln in self.playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[pln] = []
            self.userWrittenStylePlaylists[pln] = playlist_name  # for later user to display the playlist
            print("Successfully created new playlist:", self.userWrittenStylePlaylists[pln])





    def add_to_playlist(self, playlist_name, video_id):
        
        pln = playlist_name.lower()
        video = self._video_library.get_video(video_id)

        if self.is_playlist_exist(pln):

            if video != None:
                if (video.flagged == None):
                    if video in self.playlists[pln]:
                        print("Cannot add video to " + playlist_name + ": Video already added")
                    else:
                        self.playlists[pln].append(video)
                        print("Added video to " + playlist_name + ":", video._title)
                else:
                    print("Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " + \
                          video.flagged + ")")
            else:
                print("Cannot add video to " + playlist_name + ": Video does not exist")

        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")







    def show_all_playlists(self):
        """Display all playlists."""
        # print("show_all_playlists needs implementation")
        if (len(self.playlists.keys()) == 0):  # means no playlist added
            print("No playlists exist yet")

        else:
            print("Showing all playlists: ")
            for playlist in sorted(self.playlists.keys()):
                print("   " + self.userWrittenStylePlaylists[playlist.lower()])

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        # print("show_playlist needs implementation")
        pln = playlist_name.lower()

        if self.is_playlist_exist(pln):
            videos = self.playlists[pln]
            print("Showing playlist:", playlist_name)

            if len(videos) != 0:
                for vid in videos:
                    print("  ", self.get_video_details(vid))

            else:
                print("  ", "No videos here yet")
        else:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # print("remove_from_playlist needs implementation")

        pln = playlist_name.lower()
        video = self._video_library.get_video(video_id)

        if self.is_playlist_exist(pln):

            if video != None:
                if video in self.playlists[pln]:
                    print("Removed video from " + playlist_name + ":", video._title)
                    self.playlists[pln].remove(video)
                else:
                    print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
            else:
                print("Cannot remove video from " + playlist_name + ": Video does not exist")
        else:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        # print("clears_playlist needs implementation")

        pln = playlist_name.lower()
        if self.is_playlist_exist(pln):
            self.playlists[pln] = []
            print("Successfully removed all videos from " + playlist_name)
        else:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        # print("deletes_playlist needs implementation")

        pln = playlist_name.lower()
        if self.is_playlist_exist(pln):
            self.playlists.pop(pln)
            print("Deleted playlist: " + pln)
        else:
            print("Cannot delete playlist " + pln + ": Playlist does not exist")

    # ======================================= PART 3
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        # print("search_videos needs implementation")
        all_videos = self._video_library.get_all_videos()

        response_vid = []
        for video in all_videos:
            if (video.flagged == None):
                if search_term.lower() in video._title.lower():
                    response_vid.append(video)

        if (len(response_vid) != 0):
            i = 1
            print("Here are the results for " + search_term + ":")
            for rvid in response_vid:
                print("  ", str(i) + ")", self.get_video_details(rvid))
                i += 1

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            val = input()
            if (val.isnumeric()):
                _index = int(val)
                if _index > 0 and _index <= len(response_vid):
                    self.play_video(response_vid[_index - 1]._video_id)
            # else:
            #     print("")
        else:
            print("No search results for", search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        # print("search_videos_tag needs implementation")
        all_videos = self._video_library.get_all_videos()

        response_vid = []
        for video in all_videos:
            if (video.flagged == None):
                if video_tag in video._tags:
                    response_vid.append(video)

        if (len(response_vid) != 0):
            i = 1
            print("Here are the results for " + video_tag + ":")
            for rvid in response_vid:
                print("  ", str(i) + ")", self.get_video_details(rvid))
                i += 1

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            val = input()
            if (val.isnumeric()):
                _index = int(val)
                if _index > 0 and _index <= len(response_vid):
                    self.play_video(response_vid[_index - 1]._video_id)
            # else:
            #     print("")
        else:
            print("No search results for", video_tag)

    # ======================================= PART 4
    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        # print("flag_video needs implementation")
        video = self._video_library.get_video(video_id)

        # if not reason is provided
        if (flag_reason == ""):
            flag_reason = "Not supplied"

        if video != None:
            if (video.flagged == None):

                # if it is the same video that is playing then stop it only
                if (self.video_under_process.video != None):
                    if (video_id == self.video_under_process.video._video_id):
                        if (
                                self.video_under_process.status == video_state.Playing or self.video_under_process.status == video_state.Pause):
                            self.video_under_process.set_status(video_state.Stop)

                video.flagged = flag_reason
                print("Successfully flagged video:", video._title + " (reason: " + video.flagged + ")")

            else:
                print("Cannot flag video: Video is already flagged")

        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        # print("allow_video needs implementation")

        video = self._video_library.get_video(video_id)

        if video != None:
            if (video.flagged != None):
                video.flagged = None
                print("Successfully removed flag from video:", video._title)

            else:
                print("Cannot remove flag from video: Video is not flagged")

        else:
            print("Cannot remove flag from video: Video does not exist")