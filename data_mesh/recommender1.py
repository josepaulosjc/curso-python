# datamesh precisa ser implementado
# DataProduct e S3Bucket são classes para implementação
# vários imputs mas um só output que é o Bucket s3

from datamesh import *


def lambda_processing(last_sucess_data, inputs, outputs):
    all_orders = inputs["store.orders"].query("select ...")  # sql query
    reviews = inputs["imbd.reviews"].object_list()  # s3 bucket
    # process then save
    for user_id in all_users:
        outputs["recommendations"].save("today-recommendations.parquet")

# EXEMPLO 1
data_product = DataProduct(id="recommender.video",
                           inputs=["imdb.reviews#batch",
                                   "goodreads.reviews#batch",
                                   "alexa.queries#batch",
                                   "store.orders#sql"],
                           outputs={"batch": S3Bucket()},
                           processor=lambda_processing)

# EXEMPLO 2
data_product = DataProduct(id="recommender.video",
                           inputs=["imdb.reviews#batch",
                                   "goodreads.reviews#batch",
                                   "alexa.queries#batch",
                                   "geo.list#file",
                                   ["custom.s3", S3Bucket("custom_s3_bucket")]],
                           outputs={"recommendations": S3Bucket()},
                           processor=AirFlow(configuration))

# EXEMPLO 3
data_product = DataProduct(id="twitch.topics",
                           inputs=["classifier.topics#batch","twitch.videos#batch"
                                   ["custom.s3", S3Bucket("custom_s3_bucket")]],
                           outputs={"batch": S3Bucket(),
                                    "events": SNS()})



