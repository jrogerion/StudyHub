#!/bin/bash

# Script simples de Backup para Linux

# Configurações
BACKUP_DIR="/caminho/para/backups"  # Diretório onde os backups serão armazenados
SOURCE_DIRS=("/caminho/para/dados1" "/caminho/para/dados2")  # Diretórios a serem copiados
BACKUP_NAME="backup_$(date +%Y%m%d_%H%M%S)"  # Nome do arquivo de backup
MAX_BACKUPS=5  # Número máximo de backups

# Verificar se o diretório de backup existe, caso contrario, cria o diretório.
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Diretório de backup criado em $BACKUP_DIR"
fi

# Criar backup
echo "Iniciando backup dos diretórios..."
tar -czf "$BACKUP_DIR/$BACKUP_NAME.tar.gz" "${SOURCE_DIRS[@]}" 2>/dev/null

# Verificar se o backup foi criado com sucesso
if [ $? -eq 0 ]; then
    echo "Backup concluído com sucesso: $BACKUP_NAME.tar.gz"
else
    echo "Erro ao criar o backup!"
    exit 1
fi

# Remover backups antigos
echo "Verificando backups antigos..."
cd "$BACKUP_DIR" || exit
BACKUP_COUNT=$(ls -1 *.tar.gz 2>/dev/null | wc -l)

if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
    echo "Removendo backups antigos..."
    ls -t *.tar.gz | tail -n +$(($MAX_BACKUPS + 1)) | xargs rm -f
fi

echo "Operação de backup concluída."
