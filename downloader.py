from pytube import YouTube
from log import log_generator


class youtube_functions:
    def Download(link):
        error = 0
        if 'www.youtube.com' in link:
            ytObject = YouTube(link) #Creating object from YouTube class passing the link as attribute
            ytObject = ytObject.streams.get_highest_resolution() # Getting the highest quality
            error = 0
        else:
            error = 1
        

        if error == 0:
            try:
                ytObject.download()
            except Exception as e:
                print('Some error ocurred with download')
                log_generator.log_error(e)
            print('The download has been successfuly!')
        else:
            print(link)
            print('This is not a youtube video. Try it again!')

    def get_general_info(link):
        ytObject = YouTube(link)

        try:
            author = ytObject.author
            channel_url = ytObject.channel_url
            description = ytObject.description
            title = ytObject.title
            
        except UnboundLocalError:
            print('It was not possible to search for these informations :(')
            
        except Exception as e:
            print(f'Error!\n{e}')

        informations = f'''Title: {title}\nAuthor: {author}\nDescription: \n\n{description}\nChannel Url: {channel_url}\n\nHope you enjoy! :)
        '''

        return informations