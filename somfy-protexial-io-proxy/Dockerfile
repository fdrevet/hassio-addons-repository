ARG BUILD_FROM
FROM $BUILD_FROM

COPY app/ /app/

WORKDIR /app

ENTRYPOINT ["dotnet", "/app/SomfyProtexialIO.Proxy.Hassio.dll"]