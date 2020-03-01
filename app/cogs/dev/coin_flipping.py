import discord
from discord.ext import commands
from random import random, randrange, uniform


class CoinFlipping(commands.Cog):
    SEQUENCES = [["H", "H", "H", "H", "H"],
                 ["T", "T", "T", "T", "T"],
                 ["H", "T", "H", "T", "H"],
                 ["H", "H", "T", "H", "H"],
                 ["T", "T", "H", "T", "H"]]

    def __init__(self, client):
        self.client = client
        self.is_seq = False
        self.current_seq = []
        self.seq_pos = -1
        self.trick = False

    @commands.command()
    async def flip(self, ctx, choice: str) -> None:
        if choice != "H" and choice != "T":
            return
        
        choice = choice.upper()
        if self.is_seq:
                side = self.current_seq[self.seq_pos]
                self.seq_pos = self.seq_pos + 1
                if self.seq_pos >= len(self.current_seq):
                    self.is_seq = False
                    self.current_seq = []
                    self.seq_pos = -1
        else:
            if random() < 0.1:
                self.is_seq = True
                self.current_seq = CoinFlipping.SEQUENCES[randrange(len(CoinFlipping.SEQUENCES))]
                side = self.current_seq[0]
                self.seq_pos = 1
            else:
                side = "H" if random() < 0.5 else "T"
        self.trick = uniform(0, 0.1) > 0.9
        if self.trick:
            if self.is_seq or choice == side:
                side = "H" if side == "T" else "T"
            self.trick = False
        if choice == side:
            await ctx.send("You won!")
        else:
            await ctx.send("You lost!")


def setup(client):
    client.add_cog(CoinFlipping(client))

