class Book:
    def __init__(self, book_data_lst):
        self.data_val = {
            "title": book_data_lst[0],
            "author": book_data_lst[1],
            "google_id": book_data_lst[2],
            "recommender": book_data_lst[3],
            "recommended": book_data_lst[4],
            "category": book_data_lst[5],
            "publication": book_data_lst[6],
            "pages": book_data_lst[7]
        }

    def get_book_data(self):
        multiline = """
        Title: {0}
        Author: {1}
        Recommended By: {2}
        Celebrity Recommendations: {3}
        Category: {4}
        Publication: {5}
        Pages Total: {6}""".format(self.data_val["title"],
                         self.data_val["author"],
                         self.data_val["recommender"].replace("|", "\n                        "),
                         self.data_val["recommended"],
                         self.data_val["category"],
                         self.data_val["publication"],
                         self.data_val["pages"])

        print(multiline)