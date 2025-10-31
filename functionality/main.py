import yt_dlp

url = r'https://www.youtube.com/watch?v=jtLz-MFOTQQ&pp=0gcJCQMKAYcqIYzv'



def download_video(url: str, format_id, output_path='') -> str:
    """
    downloads a YouTube video/audio at <url>
    Parameters:
        url (str): Url of the target video
        format_id (str): identity of the format you need to download
            (Note: use ```list_formats``` to retrieve suitable format_id)
        output_path (str): Location to save the downloaded video/audio at.
    
    Returns:
        str: Message about whether the download was a success or not
    """

    ydl_options = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s'
    }



def list_formats(url: str):
    """
    Parameters:
        url (str): the target url
    Returns the available download formats for <url>
    
    Returns:
        dict: a dict with the following keys:
        title: video title
        audio_formats: list of dicts, with each dict representing an audio format
        video_formats: list of dicts, with each dict representing an video format
    
    # Keys of each dict in audio_format and video_format:
        format_id, resolution, acodec, vcodec

    """
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats')
    

    audio_formats = []
    video_formats = []
    
    standard_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
    
    for format in formats:
        # parsing useful data form each format dict
        resolution = format.get('format_note','')
        acodec = format.get('acodec', 'none')
        vcodec = format.get('vcodec', 'none')
        format_id = format.get('format_id', '')

        if acodec != 'none' and vcodec == 'none':
            audio_formats.append({
                'format_id': format_id,
                'resolution': resolution,
                'acodec': acodec,
                'vcodec': vcodec,
            })

# print statements only for debugging
            
            # print(f"ID: {format_id:>6} | {resolution:>10} | "
            # f"Video codec: {vcodec} | Audio codec: {acodec}")
        
        elif acodec != 'none' and vcodec != 'none' and resolution in standard_resolutions:
            video_formats.append({
                'format_id': format_id,
                'resolution': resolution,
                'acodec': acodec,
                'vcodec': vcodec,
            })
    
            # print(f"ID: {format_id:>6} | {resolution:>10} | "
            # f"Video codec: {vcodec} | Audio codec: {acodec}")

    return {
        'title': info_dict.get('title'),
        'audio_formats': audio_formats,
        'video_formats': video_formats,
        }

        
    
        
list_formats(r'https://www.youtube.com/watch?v=PssKpzB0Ah0')
