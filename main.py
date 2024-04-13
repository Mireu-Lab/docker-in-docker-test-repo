import docker

cli = docker.from_env()
dockerhub = cli.login(
    email ="limmireu1214@gmail.com", 
    username="mireulabs", 
    password="vAx!83%#@U*8Ltb", 
    registry="https://index.docker.io/v1/"
)

dockerfile_path = "/home/Hosting/workspace/app/Dockerfile"

image_name = "mireulabs/test"
image_tag = "latest"

build_config = {
    "path": dockerfile_path,
    "tag": f"{image_name}:{image_tag}"
}

if __name__ == "__main__":
    images, logs = cli.images.build(
        buildconfig = build_config
    )

    print(f"Successfully built image: {images[0].id}")

    resp = images.api.push(
            repository = image_name, 
            tag = image_tag,
            auth_config = dockerhub,
            stream = True,
            decode = True
        )

    for line in resp:
        print(line)