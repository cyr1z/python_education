ARG ALPINE_TAG="3.13.5"
FROM alpine:$ALPINE_TAG

COPY . /app
WORKDIR /app
CMD ["/bin/sh", "time_woodpeker.sh"]
