def filter_anime(anime: list):
    """Filter anime from list

    Args:
        anime (list): list of anime

    Returns:
        list: filtered anime list
    """
    used_anilists = []
    filtered_results = []
    for result in anime:
        if result["anilist"] not in used_anilists:
            used_anilists.append(result["anilist"])
            if result["similarity"] > 0.9:
                filtered_results.append(result)

    return filtered_results
