# where am I running?
# Get the directory of the currently running script
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
MAN_PY_DIR="$SCRIPT_DIR/../fc/"
VUE_DIR="${SCRIPT_DIR}/../frontend/"

# Start Django server in a screen session named "FullContact"
echo "Starting Django server at $MAN_PY_DIR ..."
source ~/venvs/fcvenv/bin/activate
screen -S FullContact -dm bash -c "cd ${MAN_PY_DIR} && screen -t django python manage.py runserver"
deactivate

# Start Vue.js server in the same screen session "FullContact"
echo "Starting Vue.js server at $VUE_DIR ..."
screen -S FullContact -X screen bash -c "cd ${VUE_DIR} && screen -t vue npm run dev"
