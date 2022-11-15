class Meta:

    def __init__(self, mname=str(), cname=str(), comicURLs=dict()):
        self.mname = mname
        self.cname = cname
        self.comicURLs = comicURLs

    def meta(self):

        path = None
        uploadURLs = list()

        for entry in self.comicURLs:
            path = "/" + self.mname + "/" + self.cname + "/" + str(entry)
            uploadURLs.append(path)

        return uploadURLs
