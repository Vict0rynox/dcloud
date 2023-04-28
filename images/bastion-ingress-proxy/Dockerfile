ARG ARCH
FROM alpine AS builder
RUN echo "Building for ${ARCH}"

FROM builder AS arm64v8
RUN echo "Building for arm64"
FROM arm64v8/nginx:latest

FROM builder AS amd64
RUN echo "Building for amd64"
FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
