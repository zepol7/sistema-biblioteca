pipeline {
    agent any
    
    // Variables de entorno
    environment {
        PROJECT_NAME = 'Sistema Biblioteca'
        PYTHON_CMD   = 'python3'
        TEST_DIR     = 'tests'
        SRC_DIR      = 'src'
    }
    
    // Configuración del pipeline
    options {
        timeout(time: 30, unit: 'MINUTES')     // Máximo 30 min
        buildDiscarder(logRotator(numToKeepStr: '10')) // Guardar 10 builds
        timestamps()                             // Mostrar tiempo en logs
    }
    
    stages {
        
        // ──────────────────────────────────────
        stage('🔽 Clonar Repositorio') {
        // ──────────────────────────────────────
            steps {
                echo "=== Iniciando build #${BUILD_NUMBER} de ${PROJECT_NAME} ==="
                echo "Rama: ${GIT_BRANCH}"
                echo "Commit: ${GIT_COMMIT}"
            }
        }
        
        // ──────────────────────────────────────
        stage('🔍 Verificar Entorno') {
        // ──────────────────────────────────────
            steps {
                echo "=== Verificando herramientas instaladas ==="
                sh "${PYTHON_CMD} --version"
                sh "git --version"
                sh "pip3 --version || pip --version"
            }
        }
        
        // ──────────────────────────────────────
        stage('📦 Instalar Dependencias') {
        // ──────────────────────────────────────
            steps {
                echo "=== Instalando dependencias del proyecto ==="
                sh """
                    ${PYTHON_CMD} -m pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No hay requirements.txt - saltando instalación de dependencias"
                    fi
                """
            }
        }
        
        // ──────────────────────────────────────
        stage('🔬 Análisis Estático (Linting)') {
        // ──────────────────────────────────────
            steps {
                echo "=== Analizando calidad del código ==="
                sh """
                    pip install pyflakes --quiet
                    ${PYTHON_CMD} -m pyflakes ${SRC_DIR}/ || true
                    echo "Análisis estático completado"
                """
            }
        }
        
        // ──────────────────────────────────────
        stage('🧪 Ejecutar Pruebas') {
        // ──────────────────────────────────────
            steps {
                echo "=== Ejecutando pruebas unitarias ==="
                sh """
                    cd ${TEST_DIR}
                    ${PYTHON_CMD} test_catalogo.py
                """
            }
            post {
                always {
                    echo "Las pruebas han terminado (exitosas o no)"
                }
                success {
                    echo "✅ Todas las pruebas pasaron"
                }
                failure {
                    echo "❌ Algunas pruebas fallaron - deteniendo pipeline"
                }
            }
        }
        
        // ──────────────────────────────────────
        stage('📊 Generar Reportes') {
        // ──────────────────────────────────────
            steps {
                echo "=== Generando reportes ==="
                sh """
                    mkdir -p reports
                    echo "Reporte de Build #${BUILD_NUMBER}" > reports/summary.txt
                    echo "Fecha: \$(date)" >> reports/summary.txt
                    echo "Rama: ${GIT_BRANCH}" >> reports/summary.txt
                    echo "Commit: ${GIT_COMMIT}" >> reports/summary.txt
                    echo "Estado: EXITOSO" >> reports/summary.txt
                    cat reports/summary.txt
                """
            }
        }
        
        // ──────────────────────────────────────
        stage('🏷️ Crear Baseline (Solo en main)') {
        // ──────────────────────────────────────
            when {
                branch 'main'
            }
            steps {
                echo "=== Creando baseline automática en rama main ==="
                sh """
                    BUILD_TAG="jenkins-build-${BUILD_NUMBER}"
                    echo "Tag de baseline: \${BUILD_TAG}"
                    echo "Este tag se crearía en el repositorio: \${BUILD_TAG}"
                """
            }
        }
        
        // ──────────────────────────────────────
        stage('🚀 Despliegue (Solo en main)') {
        // ──────────────────────────────────────
            when {
                branch 'main'
            }
            steps {
                echo "=== Simulando despliegue a producción ==="
                sh """
                    echo "Desplegando ${PROJECT_NAME} build #${BUILD_NUMBER}"
                    echo "Ambiente: PRODUCCIÓN"
                    echo "Timestamp: \$(date -u +%Y-%m-%dT%H:%M:%SZ)"
                    sleep 2
                    echo "✅ Despliegue completado exitosamente"
                """
            }
        }
    }
    
    // Acciones post-pipeline
    post {
        always {
            echo "=== Pipeline finalizado ==="
            echo "Build #${BUILD_NUMBER} - Estado: ${currentBuild.currentResult}"
        }
        success {
            echo "🎉 Pipeline exitoso. Sistema Biblioteca desplegado correctamente."
            // En producción real: enviar email o notificación Slack
        }
        failure {
            echo "🚨 Pipeline fallido. Revisar logs del stage fallido."
            // En producción real: notificar al equipo inmediatamente
        }
        unstable {
            echo "⚠️ Pipeline inestable. Algunas pruebas fallaron pero el build continuó."
        }
    }
}