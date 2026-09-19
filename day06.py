class DataPipeline:
    def __init__(self, name, record_count, status):
        self.name = name
        self.record_count = record_count
        self.status = status

    def is_successful(self):
        return self.status == "success"


pipeline = DataPipeline("customer_master", 250000, "success")
print(pipeline.is_successful())
