while true
do
  inotifywait -qq -r -e create,close_write,modify,move,delete ./ && pytest ./1
done