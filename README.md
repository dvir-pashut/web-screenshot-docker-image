# web-screenshot-docker-image

[![CI](https://github.com/dvir-pashut/web-screenshot-docker-image/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/dvir-pashut/web-screenshot-docker-image/actions/workflows/docker-image.yml)


### "web-screenshot-docker-image" is a repository that contains the Dockerfile and the nessesery files to create the screenshot docker image


## Usage

of course you should start by making sure that you have docker installed (daaaa). if not, refer to [docker docomentations].

then run 
 
```sh
docker pull dvir33/screenshot
```
this will grab you that latest version of the docker image

if you want a specific version you can go check the repository [here] 

and then run 

```sh
docker pull dvir33/screenshot:<your chosen tag goes here>
```

then run the docker image with the following command


```sh
docker run --rm  -it -v $(pwd)/image:/app/image dvir33/screenshot  <your URL goes here>
```

this will create a new folder called image and the screenshot will be there

## Extra

in case you want to build or modify for yourself 

first clone the repo 

```sh
git clone https://github.com/dvir-pashut/web-screenshot-docker-image.git
cd web-screenshot-docker-image
```

build the docker image 

```sh
docker build -t screenshot:test .
```

and then run it 

```sh
docker run --rm  -it -v $(pwd)/image:/app/image screenshot:test  <your URL goes here>
```


and that should do it!!!!!



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

no license!!!!!!!!!!!

free software

[//]: # 

[docker docomentations]: <https://docs.docker.com/engine/install/>
[here]: <https://hub.docker.com/r/dvir33/screenshot/tags>