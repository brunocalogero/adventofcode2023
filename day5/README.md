# Some comments & learnings about part 2

## Comments

God did I struggle with part II on this one:

It was clear to me that brute forcing this was not an option.
I ended up going with the "forward-mapping" solution as I later found out on twitter. There were a few cheeky ways of solving this (example: starting from the location instead of the seed) but the forward mapping approach felt more natural to me.

Here it clearly was all about ranges:

- My solution here tries to compute new ranges every time we need to create new ranges for each map. I later found a comment when reading through reddit that well describes in a simple fashion my similar thinking [here](https://www.reddit.com/r/adventofcode/comments/18buwiz/comment/kc6nvy1/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).

## Learnings

- When things get complicated to visualise, always, always, use an easy example as input that covers as many cases as possible.
  - Indeed, here we had big numbers, things get confusing, try to keep it as stupid simple as possible for this input to make sure your algorithm is doing what it does.
  - Also, debugger is your friend.
