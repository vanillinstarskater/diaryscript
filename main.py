import os
import os.path
from datetime import datetime

if __name__ == "__main__":

    # I know hard-coding these paths is terrible design.
    # But this is only meant for me, I only make it public because I like people seeing what I've made.
    # So it's fine here.
    today: str = f"/home/vanillin/.diary/{datetime.today().strftime("%Y-%m-%d")}.txt"
    if not os.path.exists(today):
        text: str = ""

        # Daily.
        for i in os.listdir("/home/vanillin/.local/diaryscript/headers/daily/"):
            # [:-4] clips extension.
            text += f"Daily ({i[:-4]}):\n\n"
            with open(f"/home/vanillin/.local/diaryscript/headers/daily/{i}", "r") as f:
                text += f.read()
                text += "\n\n"

        text += "------------------------------\n\n\n"

        with open(today, "w") as f:
            f.write(text)

    os.system(f"nvim {today}")
