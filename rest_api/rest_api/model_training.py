from haystack.nodes import FARMReader



#reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
reader = FARMReader(model_name_or_path="/opt/rest_api/my_model", use_gpu=True)

data_dir = "data/squad20"
# data_dir = "PATH/TO_YOUR/TRAIN_DATA"
reader.train(data_dir=data_dir, train_filename="answers-v1.json", use_gpu=True, n_epochs=3, save_dir="my_model2")
reader.save(directory="my_model2")

