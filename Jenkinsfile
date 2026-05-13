pipeline {
    agent any

    environment {
        PROJECT_NAME = 'Sistema Biblioteca'
        PYTHON_CMD   = 'C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe'
        TEST_DIR     = 'tests'
        SRC_DIR      = 'src'
    }

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    stages {

        stage('Verificar Entorno') {
            steps {
                echo "=== Verificando herramientas ==="
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" --version'
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip --version'
                bat 'git --version'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo "=== Instalando dependencias ==="
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pip install pyflakes --quiet'
            }


        }

        stage('Analisis de Codigo') {
            steps {
                echo "=== Analizando calidad del codigo ==="
                bat '"C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" -m pyflakes src/ || exit 0'                
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                echo "=== Ejecutando pruebas unitarias ==="
                bat 'cd tests && "C:\\Users\\helio.lopez_davinci\\AppData\\Local\\Python\\bin\\python.exe" test_catalogo.py'
            }
            post {
                success {
                    echo "Todas las pruebas pasaron correctamente"
                }
                failure {
                    echo "Algunas pruebas fallaron - pipeline detenido"
                }
            }
        }

        stage('Generar Reporte') {
            steps {
                echo "=== Generando reporte de build ==="
                bat '''
                    if not exist reports mkdir reports
                    echo ================================  > reports\\summary.txt
                    echo REPORTE BUILD #%BUILD_NUMBER%   >> reports\\summary.txt
                    echo ================================ >> reports\\summary.txt
                    echo Proyecto : %PROJECT_NAME%       >> reports\\summary.txt
                    echo Fecha    : %DATE% %TIME%        >> reports\\summary.txt
                    echo Estado   : EXITOSO              >> reports\\summary.txt
                    echo ================================ >> reports\\summary.txt
                    type reports\\summary.txt
                '''
            }
        }

        stage('Crear Baseline') {
            when {
                branch 'main'
            }
            steps {
                echo "=== Creando baseline en rama main ==="
                bat 'echo Baseline jenkins-build-%BUILD_NUMBER% creada'
            }
        }

        stage('Despliegue') {
            when {
                branch 'main'
            }
            steps {
                echo "=== Simulando despliegue a produccion ==="
                bat '''
                    echo Desplegando %PROJECT_NAME%...
                    echo Build numero : %BUILD_NUMBER%
                    echo Ambiente     : PRODUCCION
                    echo Estado       : Despliegue exitoso
                '''
            }
        }
    }

    post {
        always {
            echo "=== Pipeline finalizado ==="
            echo "Build #${BUILD_NUMBER} - Resultado: ${currentBuild.currentResult}"
        }
        success {
            echo "Pipeline exitoso. Sistema Biblioteca listo."
        }
        failure {
            echo "Pipeline fallido. Revisar el stage en rojo."
        }
        unstable {
            echo "Pipeline inestable. Algunas pruebas fallaron."
        }
    }
}