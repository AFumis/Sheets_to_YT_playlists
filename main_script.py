from get_data_from_sheets import get_sheet
from playlists_aux import list_existing_playlists, create_playlist, delete_playlist, \
    list_videos_in_playlist, add_to_playlist

def main():
    # create_playlist("Hype Xenoblade Chronicles Music")
    # create_playlist("Calm Xenoblade Chronicles Music")

    # print(list_existing_playlists())

    sheet = get_sheet()

    hype_xeno_playlistId = "PLxNYnA9cSFOOAqbGXeUukJco4kmdc9eUj"
    calm_xeno_playlistId = "PLxNYnA9cSFON6wJfChW1vJFJPvxGj_M_x"

    in_hype_xeno = list_videos_in_playlist(hype_xeno_playlistId)
    in_calm_xeno = list_videos_in_playlist(calm_xeno_playlistId)

    add_to_hype_xeno = sheet.query(
        "Franquia == 'Xenoblade Chronicles' and Estilo in ['Animada', 'Épica'] and videoId not in @in_hype_xeno['videoId']"
    )["videoId"].tolist()
    add_to_calm_xeno = sheet.query(
        "Franquia == 'Xenoblade Chronicles' and Estilo in ['Calminha', 'Feliz'] and videoId not in @in_calm_xeno['videoId']"
    )["videoId"].tolist()

    add_to_playlist(
        playlist=hype_xeno_playlistId,
        videos=add_to_hype_xeno
    )
    add_to_playlist(
        playlist=calm_xeno_playlistId,
        videos=add_to_calm_xeno
    )

if __name__ == '__main__':
    main()
