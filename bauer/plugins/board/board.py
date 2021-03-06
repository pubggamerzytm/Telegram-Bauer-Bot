import bauer.emoji as emo
import bauer.utils as utl
import math

from bauer.plugin import BauerPlugin
from telegram import ParseMode


class Board(BauerPlugin):

    @BauerPlugin.threaded
    @BauerPlugin.send_typing
    def execute(self, bot, update, args):
        if not args:
            update.message.reply_text(
                text=f"Usage:\n{self.get_usage()}",
                parse_mode=ParseMode.MARKDOWN)
            return

        args = [s.lower() for s in args]

        # --- RAIN toplist ----
        if args[0] == "rain":

            # ---- Who gave the most ----
            sql = self.get_resource("rain_giver.sql")
            res = self.execute_sql(sql, plugin="rain")

            if not res["success"]:
                update.message.reply_text(
                    text=f"{emo.ERROR} {res['data']}",
                    parse_mode=ParseMode.MARKDOWN)
                return

            length = 0
            first = True
            msg = f"*Rain Toplist*\n\nWho gave the most:\n"

            if res["data"]:
                for data in res["data"]:
                    user = f"@{utl.esc_md(data[0])}"
                    amount = f"{math.ceil(data[1] * 100) / 100:.2f}"

                    if first:
                        first = False
                        length = len(amount)

                    msg += f"`{amount:>{length}}` {user}\n"
            else:
                msg += f"{emo.INFO} No data yet\n"

            # ---- Who received the most ----
            msg += "\nWho received the most:\n"

            sql = self.get_resource("rain_taker.sql")
            res = self.execute_sql(sql, plugin="rain")

            if not res["success"]:
                update.message.reply_text(
                    text=f"{emo.ERROR} {res['data']}",
                    parse_mode=ParseMode.MARKDOWN)
                return

            length = 0
            first = True

            if res["data"]:
                for data in res["data"]:
                    user = f"@{utl.esc_md(data[0])}"
                    amount = f"{math.ceil(data[1] * 100) / 100:.2f}"

                    if first:
                        first = False
                        length = len(amount)

                    msg += f"`{amount:>{length}}` {user}\n"
            else:
                msg += f"{emo.INFO} No data yet\n"

            update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

        # ---- TIP toplist ----
        elif args[0] == "tip":

            # ---- Who gave the most ----
            sql = self.get_resource("tip_giver.sql")
            res = self.execute_sql(sql, plugin="tip")

            if not res["success"]:
                update.message.reply_text(
                    text=f"{emo.ERROR} {res['data']}",
                    parse_mode=ParseMode.MARKDOWN)
                return

            length = 0
            first = True
            msg = f"*Tip Toplist*\n\nWho gave the most:\n"

            if res["data"]:
                for data in res["data"]:
                    user = f"@{utl.esc_md(data[0])}"
                    amount = f"{math.ceil(data[1] * 100) / 100:.2f}"

                    if first:
                        first = False
                        length = len(amount)

                    msg += f"`{amount:>{length}}` {user}\n"
            else:
                msg += f"{emo.INFO} No data yet\n"

            # ---- Who received the most ----
            msg += "\nWho received the most:\n"

            sql = self.get_resource("tip_taker.sql")
            res = self.execute_sql(sql, plugin="tip")

            if not res["success"]:
                update.message.reply_text(
                    text=f"{emo.ERROR} {res['data']}",
                    parse_mode=ParseMode.MARKDOWN)
                return

            length = 0
            first = True

            if res["data"]:
                for data in res["data"]:
                    user = f"@{utl.esc_md(data[0])}"
                    amount = f"{math.ceil(data[1] * 100) / 100:.2f}"

                    if first:
                        first = False
                        length = len(amount)

                    msg += f"`{amount:>{length}}` {user}\n"
            else:
                msg += f"{emo.INFO} No data yet\n"

            update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

        # ---- Everything else ----
        else:
            update.message.reply_text(
                text=f"Usage:\n{self.get_usage()}",
                parse_mode=ParseMode.MARKDOWN)
