import torch
import torch.nn as nn
from transformers import BertModel

class BertEmbedder(nn.Module):
    def __init__(self): 
        super(BertEmbedder, self).__init__()

        self.pretrain = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True).embeddings.word_embeddings.weight
        #initialize embedding layer with bert weight
        self.embed = nn.Embedding(self.pretrain.shape[0], self.pretrain.shape[1], padding_idx=0)
        self.embed.weight.data.copy_(self.pretrain)

    def forward(self, tokens):
        return self.embed(tokens)