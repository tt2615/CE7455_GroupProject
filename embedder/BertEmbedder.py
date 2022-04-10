import torch
import torch.nn as nn
from transformers import BertModel

class BertEmbedder(nn.Module):
    def __init__(self, vocab_size, emsize, vectorizer): 
        super(BertEmbedder, self).__init__()

        self.embed = nn.Embedding(vocab_size, emsize, padding_idx=0)
       
        #initialize embedding layer with bert weight
        self.pretrain = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True).embeddings.word_embeddings.weight

        self.idx2bert = vectorizer.idx2bert
        for idx, b_idx in self.idx2bert.items():
            self.embed.weight[idx].data.copy_(self.pretrain[b_idx])

    def forward(self, tokens):
        return self.embed(tokens)