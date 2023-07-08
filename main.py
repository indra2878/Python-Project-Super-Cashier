import pandas as pd
import sys
import cashier
from cashier import Transaction

transaction_id = cashier.create_id()
transaction_id = Transaction()
transaction_id.add_item()
transaction_id.check_order()
#transaction_id.update_item()
#transaction_id.check_order()
transaction_id.delete_reset()
#transaction_id.check_discount()
transaction_id.check_out()