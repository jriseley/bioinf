import pkg_resources
import requests 

def vibrio_cholerae_replication_origin(redownload=False):
    """A function that returns a string of the replication origin of Vibrio Cholerae. 

    Args:
        redownload (bool, optional): If True, Download from bioinformaticsalgorithms.com. Otherwise use a copy bundled in the package. Defaults to False.

    Returns:
        str: A string of nucleotides, the replication origin of Vibrio cholerae. 
    """

    if redownload:
        resp = requests.get("https://bioinformaticsalgorithms.com/data/realdatasets/Replication/v_cholerae_oric.txt")

        if resp.status_code is not 200:
            raise ConnectionError("Could not obtain dataset from bioinformaticsalgorithms.com. Status: {}".format(resp.status_code))
        
        return resp.content.decode("utf-8")
    else:
        stream = pkg_resources.resource_stream(__name__, 'data/v_cholerae_oric.txt')
        return stream.readlines()[0].decode("utf-8").strip()
