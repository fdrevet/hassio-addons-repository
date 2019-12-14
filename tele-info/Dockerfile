FROM mcr.microsoft.com/dotnet/core/aspnet:3.0-buster-slim-arm32v7

COPY app/ /app/

WORKDIR /app

ENTRYPOINT ["dotnet", "/app/TeleInformation2Mqtt.dll"]
