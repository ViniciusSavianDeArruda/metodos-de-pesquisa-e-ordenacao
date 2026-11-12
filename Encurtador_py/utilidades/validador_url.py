from urllib.parse import urlparse


class ValidadorUrl:

    @staticmethod
    def is_link_valido(url_str):

        if url_str is None or url_str.strip() == "":
            return False

        link = url_str.strip()

        # Adiciona https:// caso não tenha protocolo
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "https://" + link

        try:

            url = urlparse(link)

            host = url.hostname

            if host is None or host == "":
                return False

            if "." not in host:
                return False

            if host.startswith(".") or host.endswith("."):
                return False

            return True

        except Exception:
            return False