ARG BUILD_FROM
FROM $BUILD_FROM

COPY app/ /app/

WORKDIR /app

ENTRYPOINT ["dotnet", "/app/SomfyProtexialIO.Gateway.Hassio.dll"]