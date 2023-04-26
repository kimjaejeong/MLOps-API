FROM pytorch/torchserve:0.1-cpu

COPY model-store /home/model-server/model-store

EXPOSE 8080

CMD ["torchserve", "--start", "--model-store", "model-store", "--models", "densenet161=densenet161.mar"]