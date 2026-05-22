# ── Etapa 1: compilar con Maven ──────────────────────────
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# ── Etapa 2: imagen final ─────────────────────────────────
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/jjk-service-1.0.0.jar app.jar

# Exponer puerto
EXPOSE 8080

# Variables de entorno para la base de datos
ENV SPRING_DATASOURCE_URL=jdbc:postgresql://aws-1-us-west-2.pooler.supabase.com:5432/postgres?user=postgres.cazxvbycmisoljeuonct&password=animepaswword&sslmode=require
ENV SPRING_DATASOURCE_DRIVER_CLASS_NAME=org.postgresql.Driver
ENV SPRING_JPA_HIBERNATE_DDL_AUTO=none
ENV SPRING_JPA_OPEN_IN_VIEW=false

ENTRYPOINT ["java", "-jar", "app.jar"]