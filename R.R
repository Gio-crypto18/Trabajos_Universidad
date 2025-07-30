
library(Rcmdr)
library(car)
library(RcmdrMisc)
library(RcmdrPlugin.TeachStat)
library(readxl)
library(agricolae)
library(summarytools)


 # Ver los nombres de las columnas en tu dataframe
 colnames(Reporte_Exportaciones90)
 
 library(abind,pos = 16)
 library(abind,pos = 17)
 
 knitr::opts_chunk$set(comment=NA, prompt=TRUE, out.width=750, fig.height=8, fig.width=8)
 library(Rcmdr)
 library(car)
 library(RcmdrMisc)
 library(RcmdrPlugin.TeachStat)
 library(readxl)
 
 
#LEER BASE DE DATOS ADEX 2024 
 datos_usa_2024 <- subset(Reporte_Exportaciones90, 
                          rownames=FALSE,
                          header=TRUE, na="", sheet="Reporte - Exportaciones",
                          stringsAsFactors=TRUE)
 datos_usa_2024

 #VER NOMBRES
 names(datos_usa_2024)
 
 # OBJETIVO 1: 
 #Llamar a las librerias
 knitr::opts_chunk$set(comment = NA, prompt = TRUE, out.width = 750, fig.height = 8, fig.width = 8)
 library(Rcmdr)
 library(car)
 library(RcmdrMisc)
 library(RcmdrPlugin.TeachStat)
 library(readxl)

 #PRIMERA TABLA 
 # Opción 1: Usar calcular_frecuencia() 
 calcular_frecuencia(df.nominal = datos_usa_2024[c("País", "Vía de transporte")], 
                     ordenado.frec = FALSE, 
                     df.ordinal = NULL, 
                     cuantil.p = 0.5, 
                     iprint = TRUE)
 
 # Tabla de frecuencias absolutas (cantidades)
 tabla_absoluta <- table(datos_usa_2024$País, datos_usa_2024$`Vía de transporte`)
 print("Tabla de Frecuencias Absolutas:")
 print(tabla_absoluta)

 
 # SEGUNDA TABLA
 tabla_con_totales <- addmargins(tabla_absoluta, margin = 1)  # margin=1 para sumar por filas (países)
 
 print("Tabla de Frecuencias Absolutas con Totales por País:")
 print(tabla_con_totales)
 
 totales_columnas <- colSums(tabla_absoluta)
 
 tabla_porcentaje_columnas <- prop.table(tabla_absoluta, margin = 2) * 100
 suma_columnas_porcentaje <- colSums(tabla_porcentaje_columnas)
 
 tabla_mostrar <- rbind(round(tabla_porcentaje_columnas, 2), "SUMA" = round(suma_columnas_porcentaje, 2))
 print(tabla_mostrar)

#que es matriz_porcentajes(valor absoluto de un país para una vía de transporte / total de esa vía de transporte) * 10
 matriz_porcentajes <- as.matrix(tabla_porcentaje_columnas) 
 
 posiciones_barras <- barplot(matriz_porcentajes,
                              main = "Distribución porcentual de exportaciones de cobre según país de destino por vía de transporte",
                              xlab = "Vía de transporte",
                              ylab = "Porcentaje de exportacion",
                              col = heat.colors(nrow(matriz_porcentajes)),
                              beside = TRUE,#barra lado a lado no apiladas
                              ylim = c(0, max(matriz_porcentajes) * 1.3))
 
 # Leyenda personalizada
 legend("topright",
        legend = rownames(matriz_porcentajes),
        title = "Países",
        title.adj = 0.3,  # Centrar título
        fill = heat.colors(nrow(matriz_porcentajes)),
        cex = 0.6,
        bty = "n",
        x.intersp = 0.8,
        y.intersp = 0.8,
        inset = c(-0.10, 0))
 
 # Añadir porcentajes
 text(x = posiciones_barras,
      y = matriz_porcentajes + 5,
      labels = paste0(round(matriz_porcentajes, 1), "%"),
      cex = 0.7)
 

 #OBJETIVO 2
 
 knitr::opts_chunk$set(comment=NA, prompt=TRUE, out.width=750, fig.height=8, fig.width=8)
 library(Rcmdr)
 library(car)
 library(RcmdrMisc)
 library(RcmdrPlugin.TeachStat)
 library(readxl)
 library(agricolae)
 library(summarytools)
 
 
 #EJECUTAR PRIMERO
 # 1. Filtrar datos para ESTADOS UNIDOS 2024 (Peso Neto > 0)
 datos_usa_2024 <- subset(Reporte_Exportaciones90, 
                          País == "ESTADOS UNIDOS" & 
                            Año == 2024 &
                            `Peso Neto (Kg.)` > 0)
 
 peso_neto <- datos_usa_2024$`Peso Neto (Kg.)`
 
 # HALLAR LA AMPLITUD 
 PESONETO <- datos_usa_2024$`Peso Neto (Kg.)`
 PESONETO
 
 n <- length(PESONETO)
 k <- round(1 + 3.322*log10(n), 0) # REGLA DE STURGES
 max1 <- max(PESONETO)
 min1 <- min(PESONETO)
 r <- max1 - min1 # RANGO
 dec <- 2
 tic <- ceiling(r/k*10^dec)/10^dec
 clases <- seq(min1, max1 + tic, by = tic)
 
 # TABLA DE FRECUENCIA (usando table.freq como en el guía)
 h <- table.freq(hist(PESONETO, breaks = clases, plot = FALSE))
 h
 ##EJECUTAR HASTA ACA
 
 
 #CON CANTIDADES PRIMERO 
 
 h1 <- hist(datos_usa_2024$`Peso Neto (Kg.)`, 
            breaks = clases,
            col = "lightblue",
            xlab = "Peso neto (Kg)",
            ylab = "Número de exportaciones",
            ylim = c(0, max(h$Frequency) * 1.1),
            main = "Distribución de pesos netos")
 
 
 # Histograma DE FRECUENCIAS PORCENTUALES
 h2 <- h1
 h2$counts <- h$Percentage
 # Volver a graficar con los valores corregidos
 plot(h2, col = "blue", border = "black",
      xlab = "Peso neto(kg)", 
      ylab = "Porcentaje de exportaciones de cobre(%)",
      main = "Distribucion porcentual de exportaciones de cobre segun peso neto(kg) a EEUU en el 2024",
      ylim = c(0, max(h2$counts) * 1.1))
 # Agregamos etiquetas con los porcentajes sobre cada barra
 text(h2$mids, h2$counts + 1, 
      labels = paste0(round(h2$counts, 1), "%"), 
      cex = 0.8, col = "black")
 #FIN
   
# OBJETIVO 3
   # INICIO
   knitr::opts_chunk$set(comment=NA, prompt=TRUE, out.width=750, fig.height=8, fig.width=8)
   library(Rcmdr)
   library(car)
   library(RcmdrMisc)
   library(RcmdrPlugin.TeachStat)
   library(readxl)
   library(agricolae)
   library(summarytools)
   library(dplyr)
   library(tidyr)
   
   # Opciones para formato numérico
   options(scipen = 999)  # Desactiva notación científica
   options(digits = 8)    # Muestra hasta 8 dígitos
   
   # EJECUTAR PRIMERO
   # 1. Filtrar datos para ESTADOS UNIDOS 2024 (Peso Neto > 0)
   datos_usa_2024 <- subset(Reporte_Exportaciones90, 
                            Año == 2024 &
                              `Peso Neto (Kg.)` > 0)
   
   peso_neto <- datos_usa_2024$`Peso Neto (Kg.)`
   
   # Verificación de estructura
   if(!"US$ FOB" %in% names(datos_usa_2024)) {
     # Intento encontrar la columna correcta
     posibles_nombres <- c("US$ FOB", "Valor_FOB", "FOB_USD", "Valor FOB")
     nombre_correcto <- posibles_nombres[posibles_nombres %in% names(datos_usa_2024)]
     
     if(length(nombre_correcto) > 0) {
       datos_usa_2024 <- rename(datos_usa_2024, `US$ FOB` = !!sym(nombre_correcto[1]))
       message("Columna renombrada a 'US$ FOB' desde: ", nombre_correcto[1])
     } else {
       stop("No se encontró la columna con los valores FOB. Nombres buscados: ", 
            paste(posibles_nombres, collapse = ", "))
     }
   }
   
   # Función para calcular moda mejorada
   Mode <- function(x) {
     x <- na.omit(x)
     if(length(x) == 0) return(NA)
     ux <- unique(x)
     ux[which.max(tabulate(match(x, ux)))]
   }
   
   # Cálculo de estadísticas (versión mejorada con nuevas medidas)
   estadisticas_por_puerto <- datos_usa_2024 %>%
     filter(Puerto %in% c("BALBOA", "MIAMI")) %>%
     group_by(Puerto) %>%
     summarise(
       # Medidas de tendencia central
       Media = mean(`US$ FOB`, na.rm = TRUE),
       `Error típico` = sd(`US$ FOB`, na.rm = TRUE) / sqrt(sum(!is.na(`US$ FOB`))),
       Mediana = median(`US$ FOB`, na.rm = TRUE),
       Moda = Mode(`US$ FOB`),
       
       # Medidas de dispersión (ampliadas)
       `Desviación estándar` = sd(`US$ FOB`, na.rm = TRUE),
       `Varianza de la muestra` = var(`US$ FOB`, na.rm = TRUE),
       Rango = max(`US$ FOB`, na.rm = TRUE) - min(`US$ FOB`, na.rm = TRUE),
       RIC = IQR(`US$ FOB`, na.rm = TRUE),  # Rango intercuartílico
       CV = (sd(`US$ FOB`, na.rm = TRUE)/mean(`US$ FOB`, na.rm = TRUE))*100,  # Coeficiente de variación
       
       # Medidas de forma
       Curtosis = ifelse(n() > 3, e1071::kurtosis(`US$ FOB`, na.rm = TRUE), NA),
       `Coeficiente de asimetría` = ifelse(n() > 2, e1071::skewness(`US$ FOB`, na.rm = TRUE), NA),
       
       # Medidas de posición (nueva sección)
       Mínimo = min(`US$ FOB`, na.rm = TRUE),
       `Percentil 25` = quantile(`US$ FOB`, probs = 0.25, na.rm = TRUE),
       `Percentil 50` = quantile(`US$ FOB`, probs = 0.50, na.rm = TRUE),
       `Percentil 75` = quantile(`US$ FOB`, probs = 0.75, na.rm = TRUE),
       Máximo = max(`US$ FOB`, na.rm = TRUE),
       
       # Totales
       Suma = sum(`US$ FOB`, na.rm = TRUE),
       Cuenta = sum(!is.na(`US$ FOB`))
     ) %>%
     mutate(across(where(is.numeric), ~ifelse(is.nan(.) | is.infinite(.), NA, .))) %>%
     mutate(across(where(is.numeric), round, 2))  # Redondeo a 2 decimales
   
   # Formateo de tabla (versión mejorada con nuevas categorías)
   tabla_formateada <- estadisticas_por_puerto %>%
     pivot_longer(cols = -Puerto, names_to = "Indicador") %>%
     pivot_wider(names_from = Puerto, values_from = value) %>%
     mutate(Categoría = case_when(
       Indicador %in% c("Media", "Mediana", "Moda") ~ "Tendencia Central",
       Indicador %in% c("Error típico", "Desviación estándar", "Varianza de la muestra", 
                        "Rango", "RIC", "CV") ~ "Dispersión",
       Indicador %in% c("Curtosis", "Coeficiente de asimetría") ~ "Forma",
       Indicador %in% c("Mínimo", "Percentil 25", "Percentil 50", 
                        "Percentil 75", "Máximo") ~ "Posición",
       TRUE ~ "Totales"
     )) %>%
     select(Categoría, Indicador, BALBOA, MIAMI) %>%
     arrange(factor(Categoría, levels = c("Tendencia Central", "Dispersión", "Forma", "Posición", "Totales")),
             factor(Indicador, levels = c(
               "Media", "Mediana", "Moda", 
               "Error típico", "Desviación estándar", "Varianza de la muestra", 
               "Rango", "RIC", "CV",
               "Coeficiente de asimetría", "Curtosis",
               "Mínimo", "Percentil 25", "Percentil 50", "Percentil 75", "Máximo",
               "Suma", "Cuenta"
             )))
   
   # Visualización profesional mejorada
   cat("\nESTADÍSTICAS DESCRIPTIVAS COMPLETAS - EXPORTACIONES A ESTADOS UNIDOS\n")
   cat("==================================================================\n")
   cat("Periodo: 2024 | Puertos: BALBOA vs MIAMI\n")
   cat(paste("Total observaciones:", sum(estadisticas_por_puerto$Cuenta), "\n\n"))
   
   print.data.frame(tabla_formateada, row.names = FALSE, right = FALSE, digits = 2)
   
  # OBJ4
  # Cargar librerías
  library(Rcmdr)
  library(car)
  library(RcmdrMisc)
  library(readxl)
  library(abind, pos=16)
  library(e1071, pos=17)
  
  # Subir base de datos de exportaciones marítimas
  mar <- read_excel("maritima.xlsx", 
                    sheet = "Reporte - Exportaciones", 
                    na = "")
  
  # Calcular estadísticos para el diagrama de cajas
  minimo <- tapply(mar$`Peso Bruto (Kg.)`, mar$País, function(x) boxplot.stats(x)$stats[1])
  p25 <- tapply(mar$`Peso Bruto (Kg.)`, mar$País, function(x) boxplot.stats(x)$stats[2])
  p50 <- tapply(mar$`Peso Bruto (Kg.)`, mar$País, function(x) boxplot.stats(x)$stats[3])
  p75 <- tapply(mar$`Peso Bruto (Kg.)`, mar$País, function(x) boxplot.stats(x)$stats[4])
  maximo <- tapply(mar$`Peso Bruto (Kg.)`, mar$País, function(x) boxplot.stats(x)$stats[5])
  
  # Calcular el Rango Intercuartílico (RIC) del Peso Bruto por país
  ric <- p75 - p25
  
  # Identificar valores atípicos (usando el primer país como ejemplo)
  primer_pais <- unique(mar$País)[1]
  atipicos <- boxplot.stats(mar$`Peso Bruto (Kg.)`[mar$País == primer_pais])$out
  
  # Crear diagrama de cajas
  Boxplot(`Peso Bruto (Kg.)` ~ País, 
          data = mar,
          id = FALSE,
          xlab = "Países destino", 
          ylab = "Peso Bruto (Kg.)",
          main = "Distribución de exportaciones marítimas según peso bruto (Kg) por país de destino", 
          col = palette()[5:9])
  
  # Añadir etiquetas de valores atípicos
  if(length(atipicos) > 0) {
    for(i in 1:length(atipicos)) {
      text(1 + 0.02, atipicos[i], labels = atipicos[i], cex = 0.7, adj = 0)
    }
  }
  
  # Añadir etiquetas de estadísticos a cada caja
  for (i in 1:length(unique(mar$País))) {
    text(x = i + 0.21, y = minimo[i], labels = round(minimo[i], 2), cex = 0.7, adj = 0)
    text(x = i + 0.41, y = p25[i], labels = round(p25[i], 2), cex = 0.7, adj = 0)
    text(x = i + 0.41, y = p50[i], labels = round(p50[i], 2), cex = 0.7, adj = 0)
    text(x = i + 0.41, y = p75[i], labels = round(p75[i], 2), cex = 0.7, adj = 0)
    text(x = i + 0.21, y = maximo[i], labels = round(maximo[i], 2), cex = 0.7, adj = 0)
  }
  #fin
  
  #COMO SE HALLO EL COEFICIENTE DE VARIACION DEL OBJ3 
 # COEFICIENTE DE VARIACION
  knitr :: opts_chunk$set(comment=NA, prompt=TRUE, out.width=750,
                          fig.height=8, fig.width=8)
  library(Rcmdr)
  library(car)
  library(RcmdrMisc)
  library(readxl)
  
  datos_usa_2024 <- subset(Reporte_Exportaciones90, 
                           rownames=FALSE,
                           header=TRUE, na="", sheet="Reporte - Exportaciones",
                           stringsAsFactors=TRUE)
  datos_usa_2024
  
  numSummary(datos_usa_2024[, "US$ FOB", drop=FALSE], 
             groups=datos_usa_2024$Puerto,
             statistics=c("mean", "sd", "CV"), 
             quantiles=c(0, 0.25, 0.5, 0.75, 1))
  
  boxplot.stats(subset(mar, subset=País=="ESTADOS UNIDOS")$`Peso Bruto (Kg.)`)
  
  
  