import logging
import requests

def requesters(url: str) -> str:

    try:

        ip = requests.get('https://api.ipify.org/').text

        req = requests.get(url)
        req = str(req)

        if req == "<Response [200]>":

            logging.basicConfig(

                level       = logging.INFO,
                style       = '{',
                format      = '{asctime} {levelname:<2} {message}',
                filename    = 'mylog.log',
                filemode    = 'a+'

            )

            status = '200'

            logging.info(f'{ip} {status} {url}')

            return "Sucess 200"

        elif req == "<Response [400]>":

            logging.basicConfig(

                level       = logging.DEBUG,
                style       = '{',
                format      = '{asctime} {levelname:<2} {message}',
                filename    = 'mylog.log',
                filemode    = 'a+'

            )

            status = '400'

            logging.info(f'{ip} {status} {url}')

            return "Sucess 400"

        elif req == "<Response [500]>":

            logging.basicConfig(

                level       = logging.DEBUG,
                style       = '{',
                format      = '{asctime} {levelname:<2} {message}',
                filename    = 'mylog.log',
                filemode    = 'a+'

            )

            status = '500'

            logging.info(f'{ip} {status} {url}')

            return None

        return type(req)

    except Exception as err:

        logging.basicConfig(

            level       = logging.DEBUG,
            style       = '{',
            format      = '{asctime} {levelname:<2} {message}',
            filename    = 'mylog.log',
            filemode    = 'a+'

        )

        status = "404"

        logging.info(f'{ip} {status} {err}')

        return None

def main():

    # Example of Sucess (200)
    requesters("https://api.movidesk.com/public/v1")

    # Example of Failure (404)
    requesters("https://votation.xyz/public/v1/01032004/GustavoRodrigueess")

if __name__ == "__main__":
    main()
